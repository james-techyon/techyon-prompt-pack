# Stage 8: Legal, Security & Compliance

## Purpose
Ensure product meets all regulatory requirements and implements appropriate security controls.

## Required Inputs
- {Industry/Regulatory} context
- Data model from Stage 4
- {Geography} for jurisdiction

## Assets Produced
- Regulatory Checklist
- Data Protection Plan
- Security Baseline
- Legal Document Templates
- IP Strategy

---

## Prompt

```
Create:
- Applicable regs checklist (e.g., GDPR/CCPA/HIPAA/PCI/FINRA) given {Industry/Regulatory}
- Data flow narrative + data inventory (fields, purpose, retention)
- Security baseline (access control, encryption, logging, incident response)
- Template: Privacy Policy & Terms outline (sections + notes)
- IP strategy options (trade secret vs patent vs copyright, OSS licenses to avoid)

Call out any blocking legal work for MVP.
```

---

## Gate Check Prompt

```
Legal/compliance assessment:
- Red flag any unaddressed regulatory requirements
- Yellow flag if policies need legal review
- Green if all requirements have clear solutions
List specific legal counsel needs.
```

---

## Success Metrics
- [ ] All regulatory requirements identified
- [ ] Data protection measures implemented
- [ ] Security controls documented
- [ ] Privacy/Terms drafts complete
- [ ] IP strategy defined

## Common Pitfalls
- Discovering compliance needs late
- Underestimating legal costs
- Missing data residency requirements
- Using incompatible OSS licenses

## Next Stage
Proceed to Stage 9: Analytics & Experimentation