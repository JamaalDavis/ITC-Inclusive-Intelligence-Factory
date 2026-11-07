# The evolution of AI design: product behavior under uncertainty

Traditional software often follows deterministic rules in controlled states; actual products can still vary because of network conditions, concurrency, and external systems. Generative models are typically probabilistic and can produce different plausible answers to similar inputs.

Design implication: we cannot specify every generated sentence, but we **can** specify system boundaries, permissions, evidence requirements, escalation routes, deterministic validation checks, accessible error states, and oversight.

A hallucination is not an acceptable product outcome merely because generated models can hallucinate. Treat it as a risk to measure, detect, mitigate and communicate. Never pass factual certainty to the user without evidence.

For ITC: design (1) the experience, (2) the context provided to agents, (3) the actions agents may take, (4) the conditions for review, (5) the failure and appeal journey, and (6) the feedback loop.

The key product question changes from 'What will the interface show?' to 'What behavior is permitted, under what context, with whose authority, and how can affected people challenge the outcome?'
