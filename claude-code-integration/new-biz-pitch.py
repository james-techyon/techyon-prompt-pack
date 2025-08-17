#!/usr/bin/env python3
"""
Techyon Business Pitch Validator - Claude Code Slash Command Implementation
/new-biz-pitch command handler for systematic business idea validation
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class BusinessPitchValidator:
    """Main validator class for the new-biz-pitch command"""
    
    def __init__(self, idea_name: str, options: Dict = None):
        self.idea_name = idea_name
        self.options = options or {}
        self.output_dir = Path(options.get('output', './outputs'))
        self.current_stage = options.get('stage', 1)
        self.results = {}
        self.gate_results = {}
        
        # Set workflow mode
        if options.get('quick'):
            self.stages_to_run = [1, 2, 3]
        elif options.get('investor'):
            self.stages_to_run = [1, 2, 3, 5, 6, 12]
        else:  # full mode
            self.stages_to_run = list(range(1, 13))
    
    def run(self) -> Dict:
        """Execute the validation workflow"""
        print(f"🚀 Starting validation for: {self.idea_name}")
        print(f"📊 Mode: {self._get_mode_name()}")
        print(f"📁 Output directory: {self.output_dir}")
        print("-" * 50)
        
        # Create output directory
        self._setup_output_directory()
        
        # Initialize with orchestrator
        if not self._run_orchestrator():
            return {"status": "failed", "stage": "orchestrator"}
        
        # Run selected stages
        for stage_num in self.stages_to_run:
            if stage_num < self.current_stage:
                continue
                
            print(f"\n📍 Stage {stage_num}: {self._get_stage_name(stage_num)}")
            
            # Execute stage
            stage_result = self._execute_stage(stage_num)
            self.results[stage_num] = stage_result
            
            # Run gate check
            if self._requires_gate(stage_num):
                gate_result = self._run_gate_check(stage_num, stage_result)
                self.gate_results[stage_num] = gate_result
                
                if gate_result['decision'] == 'red':
                    print(f"🔴 Gate check failed at Stage {stage_num}")
                    return self._handle_gate_failure(stage_num)
                elif gate_result['decision'] == 'yellow':
                    print(f"🟡 Gate check requires additional validation")
                    print(f"   Recommended actions: {gate_result['actions']}")
        
        # Generate final package
        self._generate_final_package()
        
        return {
            "status": "success",
            "idea": self.idea_name,
            "stages_completed": len(self.results),
            "output_location": str(self.output_dir),
            "next_steps": self._get_next_steps()
        }
    
    def _run_orchestrator(self) -> bool:
        """Run the master orchestrator prompt"""
        variables = self._collect_variables()
        
        prompt = f"""
        You are my Product Console. Goal: drive {self.idea_name} from concept to launch-ready plan.
        
        Variables:
        {json.dumps(variables, indent=2)}
        
        Process:
        1) Validate inputs and list any missing info
        2) Produce a 1-page Working Backwards PR/FAQ
        3) Output an execution map with stages, evidence, and kill criteria
        
        Output as JSON with sections: missing_info, pr_faq, execution_map
        """
        
        # This would interface with Claude/LLM
        # For now, simulate the response
        result = {
            "pr_faq": self._generate_pr_faq(variables),
            "execution_map": self._generate_execution_map(),
            "missing_info": []
        }
        
        # Save orchestrator output
        self._save_output("00-orchestrator", result)
        return True
    
    def _execute_stage(self, stage_num: int) -> Dict:
        """Execute a specific stage and return results"""
        stage_prompts = {
            1: self._stage_problem_discovery,
            2: self._stage_market_analysis,
            3: self._stage_solution_definition,
            4: self._stage_architecture,
            5: self._stage_business_model,
            6: self._stage_go_to_market,
            7: self._stage_brand_experience,
            8: self._stage_legal_compliance,
            9: self._stage_analytics,
            10: self._stage_delivery_plan,
            11: self._stage_launch_prep,
            12: self._stage_investor_materials
        }
        
        stage_func = stage_prompts.get(stage_num)
        if stage_func:
            return stage_func()
        return {}
    
    def _stage_problem_discovery(self) -> Dict:
        """Stage 1: Problem Discovery & Customer Proof"""
        return {
            "interview_guide": self._generate_interview_guide(),
            "persona": self._generate_persona(),
            "evidence_log": self._create_evidence_log_template(),
            "problem_statement": self._generate_problem_statement()
        }
    
    def _stage_market_analysis(self) -> Dict:
        """Stage 2: Market & Competition Analysis"""
        return {
            "tam_sam_som": self._calculate_market_size(),
            "competitive_matrix": self._analyze_competition(),
            "moat_hypotheses": self._identify_moats(),
            "segmentation": self._segment_market()
        }
    
    def _stage_solution_definition(self) -> Dict:
        """Stage 3: Solution Definition & PRD"""
        return {
            "prd": self._generate_prd(),
            "user_stories": self._create_user_stories(),
            "acceptance_criteria": self._define_acceptance_criteria(),
            "success_metrics": self._define_success_metrics()
        }
    
    def _stage_business_model(self) -> Dict:
        """Stage 5: Business Model & Pricing"""
        return {
            "pricing_strategy": self._design_pricing(),
            "unit_economics": self._calculate_unit_economics(),
            "financial_model": self._build_financial_model(),
            "packaging": self._define_packaging()
        }
    
    def _stage_go_to_market(self) -> Dict:
        """Stage 6: Go-To-Market Strategy"""
        return {
            "gtm_plan": self._create_gtm_plan(),
            "messaging": self._develop_messaging(),
            "channels": self._identify_channels(),
            "sales_materials": self._create_sales_materials()
        }
    
    def _stage_investor_materials(self) -> Dict:
        """Stage 12: Investor Materials"""
        return {
            "pitch_deck": self._create_pitch_deck(),
            "executive_summary": self._write_executive_summary(),
            "six_pager": self._create_narrative_memo(),
            "data_room": self._organize_data_room()
        }
    
    # Placeholder methods for other stages
    def _stage_architecture(self) -> Dict:
        return {"status": "completed", "outputs": ["architecture.md"]}
    
    def _stage_brand_experience(self) -> Dict:
        return {"status": "completed", "outputs": ["brand_guide.md"]}
    
    def _stage_legal_compliance(self) -> Dict:
        return {"status": "completed", "outputs": ["compliance_checklist.md"]}
    
    def _stage_analytics(self) -> Dict:
        return {"status": "completed", "outputs": ["analytics_plan.md"]}
    
    def _stage_delivery_plan(self) -> Dict:
        return {"status": "completed", "outputs": ["delivery_roadmap.md"]}
    
    def _stage_launch_prep(self) -> Dict:
        return {"status": "completed", "outputs": ["launch_runbook.md"]}
    
    def _run_gate_check(self, stage_num: int, stage_result: Dict) -> Dict:
        """Run gate check for a completed stage"""
        gate_criteria = {
            1: {"threshold": 0.7, "metric": "problem_validation"},
            2: {"threshold": 100_000_000, "metric": "tam_size"},
            3: {"threshold": 0.8, "metric": "technical_feasibility"},
            5: {"threshold": 3.0, "metric": "ltv_cac_ratio"},
            6: {"threshold": 0.5, "metric": "channel_validation"}
        }
        
        if stage_num not in gate_criteria:
            return {"decision": "green", "reason": "No gate for this stage"}
        
        # Simulate gate evaluation
        # In real implementation, this would analyze stage_result
        return {
            "decision": "green",  # or "yellow" or "red"
            "evidence": ["Evidence point 1", "Evidence point 2"],
            "score": 0.85,
            "recommendation": "Proceed to next stage"
        }
    
    def _handle_gate_failure(self, stage_num: int) -> Dict:
        """Handle a failed gate check"""
        pivot_options = self._generate_pivot_options(stage_num)
        
        return {
            "status": "gate_failed",
            "failed_stage": stage_num,
            "pivot_options": pivot_options,
            "recommendation": "Consider pivot or additional validation",
            "outputs_generated": list(self.results.keys())
        }
    
    def _generate_final_package(self):
        """Generate the final output package"""
        summary = {
            "idea_name": self.idea_name,
            "validation_date": datetime.now().isoformat(),
            "stages_completed": len(self.results),
            "gate_results": self.gate_results,
            "key_outputs": self._list_key_outputs(),
            "next_steps": self._get_next_steps()
        }
        
        self._save_output("validation_summary", summary)
        self._create_index_file()
        
        print("\n✅ Validation complete!")
        print(f"📦 All outputs saved to: {self.output_dir}")
    
    # Helper methods
    def _setup_output_directory(self):
        """Create the output directory structure"""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        for subdir in ['stages', 'gates', 'assets', 'research']:
            (self.output_dir / subdir).mkdir(exist_ok=True)
    
    def _save_output(self, filename: str, content: Dict):
        """Save output to file"""
        filepath = self.output_dir / f"{filename}.json"
        with open(filepath, 'w') as f:
            json.dump(content, f, indent=2)
    
    def _collect_variables(self) -> Dict:
        """Collect or prompt for required variables"""
        return {
            "IdeaName": self.idea_name,
            "OneLine": f"Innovative solution in {self._detect_industry()}",
            "FounderGoals": "speed to revenue",
            "Audience/ICP": self._detect_audience(),
            "Problem/JobsToBeDone": "To be validated",
            "Industry/Regulatory": self._detect_industry(),
            "Constraints": {"budget": 50000, "timeline": "3 months", "team": 2},
            "KeyMetricsNorthStar": "Monthly Active Users",
            "Geography": "United States"
        }
    
    def _detect_industry(self) -> str:
        """Detect industry from idea name"""
        # Simple keyword detection
        idea_lower = self.idea_name.lower()
        if any(word in idea_lower for word in ['ai', 'ml', 'tech', 'software']):
            return "Technology"
        elif any(word in idea_lower for word in ['health', 'med', 'care']):
            return "Healthcare"
        elif any(word in idea_lower for word in ['finance', 'bank', 'pay']):
            return "Financial Services"
        return "General Business"
    
    def _detect_audience(self) -> str:
        """Detect audience from options"""
        if self.options.get('b2b'):
            return "Business professionals"
        elif self.options.get('b2c'):
            return "Consumers"
        return "To be determined"
    
    def _get_mode_name(self) -> str:
        """Get the current execution mode name"""
        if self.options.get('quick'):
            return "Quick Validation (Stages 1-3)"
        elif self.options.get('investor'):
            return "Investor Package"
        return "Full Validation (All 12 Stages)"
    
    def _get_stage_name(self, stage_num: int) -> str:
        """Get the name of a stage"""
        stage_names = {
            1: "Problem Discovery",
            2: "Market Analysis",
            3: "Solution Definition",
            4: "Architecture",
            5: "Business Model",
            6: "Go-to-Market",
            7: "Brand & Experience",
            8: "Legal & Compliance",
            9: "Analytics",
            10: "Delivery Plan",
            11: "Launch Preparation",
            12: "Investor Materials"
        }
        return stage_names.get(stage_num, f"Stage {stage_num}")
    
    def _requires_gate(self, stage_num: int) -> bool:
        """Check if a stage requires a gate check"""
        return stage_num in [1, 2, 3, 5, 6]
    
    def _get_next_steps(self) -> List[str]:
        """Generate recommended next steps"""
        return [
            "Review validation summary",
            "Conduct customer interviews",
            "Refine value proposition",
            "Build MVP prototype",
            "Test pricing with target customers"
        ]
    
    def _list_key_outputs(self) -> List[str]:
        """List key outputs generated"""
        outputs = []
        for stage_num, result in self.results.items():
            if isinstance(result, dict) and 'outputs' in result:
                outputs.extend(result['outputs'])
        return outputs
    
    def _create_index_file(self):
        """Create an index file linking all outputs"""
        index_content = f"""# {self.idea_name} - Validation Package

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Stages Completed
"""
        for stage_num in self.results.keys():
            index_content += f"- [x] Stage {stage_num}: {self._get_stage_name(stage_num)}\n"
        
        index_content += "\n## Key Documents\n"
        for output in self._list_key_outputs():
            index_content += f"- [{output}](./{output})\n"
        
        index_path = self.output_dir / "INDEX.md"
        with open(index_path, 'w') as f:
            f.write(index_content)
    
    # Content generation methods (simplified versions)
    def _generate_pr_faq(self, variables: Dict) -> str:
        return f"""
# {variables['IdeaName']} - Press Release

**SEATTLE - {datetime.now().strftime('%B %d, %Y')}**

Today we announce {variables['IdeaName']}, {variables['OneLine']}.

## The Problem
[Problem description based on validation]

## Our Solution
[Solution description]

## Customer Quote
"This solution has transformed how we work" - Early Customer

## FAQ
1. Who is this for? {variables['Audience/ICP']}
2. What problem does it solve? {variables['Problem/JobsToBeDone']}
3. When will it be available? Within {variables['Constraints']['timeline']}
[... additional FAQs ...]
"""
    
    def _generate_execution_map(self) -> List[Dict]:
        return [
            {
                "stage": 1,
                "name": "Problem Discovery",
                "evidence": "Customer interviews",
                "kill_criteria": "<70% validation",
                "timeline": "Week 1"
            },
            # ... additional stages
        ]
    
    def _generate_interview_guide(self) -> List[str]:
        return [
            "Tell me about your current workflow for [problem area]",
            "What's the most frustrating part of this process?",
            "How much time do you spend on this weekly?",
            "What have you tried to solve this?",
            "If you had a magic wand, what would the perfect solution look like?",
            # ... additional questions
        ]
    
    def _generate_persona(self) -> Dict:
        return {
            "name": "Primary User",
            "demographics": {"age": "25-45", "role": "Professional"},
            "goals": ["Efficiency", "Cost reduction", "Better outcomes"],
            "pains": ["Time consuming", "Error prone", "Expensive"],
            "jobs_to_be_done": ["Functional", "Emotional", "Social"]
        }
    
    def _create_evidence_log_template(self) -> Dict:
        return {
            "headers": ["Source", "Date", "Quote", "Tag", "Strength"],
            "entries": []
        }
    
    def _generate_problem_statement(self) -> str:
        return f"Users struggle with [specific problem] resulting in [consequences]"
    
    def _calculate_market_size(self) -> Dict:
        return {
            "TAM": 1_000_000_000,
            "SAM": 100_000_000,
            "SOM": 10_000_000,
            "methodology": "Bottom-up calculation based on user segments"
        }
    
    def _analyze_competition(self) -> List[Dict]:
        return [
            {"name": "Competitor A", "strengths": [], "weaknesses": [], "positioning": ""},
            {"name": "Competitor B", "strengths": [], "weaknesses": [], "positioning": ""}
        ]
    
    def _identify_moats(self) -> List[str]:
        return [
            "Network effects from user community",
            "Proprietary data advantage",
            "Switching costs from deep integration",
            "Brand recognition in niche"
        ]
    
    def _segment_market(self) -> List[Dict]:
        return [
            {"segment": "Enterprise", "size": 10000, "attractiveness": 8},
            {"segment": "SMB", "size": 100000, "attractiveness": 7},
            {"segment": "Startups", "size": 50000, "attractiveness": 6}
        ]
    
    def _generate_prd(self) -> str:
        return "Product Requirements Document - See template for full details"
    
    def _create_user_stories(self) -> List[Dict]:
        return [
            {"id": "US-001", "story": "As a user, I want to...", "criteria": "Given/When/Then"},
        ]
    
    def _define_acceptance_criteria(self) -> List[str]:
        return ["Criteria 1", "Criteria 2", "Criteria 3"]
    
    def _define_success_metrics(self) -> Dict:
        return {
            "north_star": "Monthly Active Users",
            "input_metrics": ["Signup Rate", "Activation Rate", "Retention"],
            "targets": {"MAU": 10000, "Retention": 0.8}
        }
    
    def _design_pricing(self) -> Dict:
        return {
            "model": "SaaS subscription",
            "tiers": [
                {"name": "Starter", "price": 29, "features": []},
                {"name": "Pro", "price": 99, "features": []},
                {"name": "Enterprise", "price": "Custom", "features": []}
            ]
        }
    
    def _calculate_unit_economics(self) -> Dict:
        return {
            "LTV": 3000,
            "CAC": 500,
            "ratio": 6.0,
            "payback_months": 6,
            "gross_margin": 0.85
        }
    
    def _build_financial_model(self) -> Dict:
        return {
            "revenue_projection": [10000, 25000, 50000],  # Monthly
            "cost_structure": {"fixed": 20000, "variable": 0.15},
            "break_even": "Month 18"
        }
    
    def _define_packaging(self) -> List[Dict]:
        return [
            {"tier": "Starter", "value_metric": "users", "limit": 5},
            {"tier": "Pro", "value_metric": "users", "limit": 50},
            {"tier": "Enterprise", "value_metric": "unlimited", "limit": None}
        ]
    
    def _create_gtm_plan(self) -> str:
        return "Go-to-Market Plan - See template for full details"
    
    def _develop_messaging(self) -> Dict:
        return {
            "positioning": "The only solution that...",
            "pillars": ["Speed", "Simplicity", "Security"],
            "tagline": "Transform your workflow"
        }
    
    def _identify_channels(self) -> List[Dict]:
        return [
            {"channel": "Content Marketing", "CAC": 100, "priority": 1},
            {"channel": "Paid Search", "CAC": 200, "priority": 2},
            {"channel": "Sales Outbound", "CAC": 500, "priority": 3}
        ]
    
    def _create_sales_materials(self) -> Dict:
        return {
            "email_sequences": ["Welcome", "Education", "Conversion"],
            "scripts": ["Discovery Call", "Demo", "Close"],
            "objection_handlers": ["Price", "Features", "Timing"]
        }
    
    def _create_pitch_deck(self) -> List[str]:
        return [
            "Title Slide",
            "Problem",
            "Solution",
            "Market",
            "Product",
            "Business Model",
            "Go-to-Market",
            "Competition",
            "Team",
            "Ask"
        ]
    
    def _write_executive_summary(self) -> str:
        return "Executive Summary - 1 page overview of the opportunity"
    
    def _create_narrative_memo(self) -> str:
        return "6-page narrative memo in Amazon style"
    
    def _organize_data_room(self) -> List[str]:
        return [
            "Financial Model",
            "Customer Testimonials",
            "Product Demo",
            "Legal Documents",
            "Team Bios"
        ]
    
    def _generate_pivot_options(self, failed_stage: int) -> List[Dict]:
        return [
            {"type": "Customer Segment", "description": "Target different users"},
            {"type": "Problem", "description": "Solve adjacent problem"},
            {"type": "Solution", "description": "Different technical approach"},
            {"type": "Business Model", "description": "Change monetization"}
        ]


def main():
    """Main entry point for the command"""
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: /new-biz-pitch <idea_name> [options]")
        sys.exit(1)
    
    idea_name = sys.argv[1]
    
    # Parse options
    options = {}
    for arg in sys.argv[2:]:
        if arg.startswith('--'):
            key = arg[2:].split('=')[0]
            value = True if '=' not in arg else arg.split('=')[1]
            options[key] = value
    
    # Run validator
    validator = BusinessPitchValidator(idea_name, options)
    result = validator.run()
    
    # Output result
    print("\n" + "=" * 50)
    print("VALIDATION COMPLETE")
    print("=" * 50)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()