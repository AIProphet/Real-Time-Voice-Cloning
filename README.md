# Voice Transfer Across Languages

### Papers 
| URL | Designation | Title |
| --- | ------------ | ----- |
|[**1806.04558**](https://arxiv.org/pdf/1806.04558.pdf) | **SV2TTS** | **Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis** |
|[1802.06006](https://arxiv.org/pdf/1802.06006.pdf) | / | Neural Voice Cloning with a Few Samples |
|[1712.05884](https://arxiv.org/pdf/1712.05884.pdf) | Tacotron 2 | Natural TTS Synthesis by Conditioning Wavenet on Mel Spectrogram Predictions |
|[1710.10467](https://arxiv.org/pdf/1710.10467.pdf) | GE2E | Generalized End-To-End Loss for Speaker Verification |
|[1509.08062](https://arxiv.org/pdf/1509.08062.pdf) | TE2E | End-to-End Text-Dependent Speaker Verification |
|[1409.0473](https://arxiv.org/pdf/1409.0473.pdf) | Attention | Neural Machine Translation by Jointly Learning to Align and Translate |


### Task list
*In no particular order:*
- [x] Reformulate the subject and a short description of how the implementation will work
- [x] Finish the analysis of SV2TTS
- Other papers to read:
  - [x] Tacotron 2 (base for the synthesizer and vocoder of SV2TTS)
  - [ ] GE2E (base for the encoder of SV2TTS)
  - [ ] TE2E (base for GE2E)
  - [ ] Attention (to learn about the attention layer)
  - [ ] Tacotron 1
- [ ] Reformat my paper/dataset notes in markdown (?)
- [ ] Get started on the SOTA review
- [ ] Get started on the description of SV2TTS 
- [ ] Get started on the analysis of the benchmarks in SV2TTS 

### Roadmap
**For the 19th of October**:
- Review the current SOTA  (weaknesses/strengths w.r.t. SV2TTS)
- Complete description of the architecture of SV2TTS (embedded models, exotic layers)
- Analysis of the benchmarks (data used, metrics)

**For later**:
- Implement SV2TTS as a baseline
- Evaluate the quality of this baseline w.r.t. the reported results in SV2TTS

**For much later**:
- Adapt/Improve the cross-language aspect from the baseline

### Other things
- Setup Matheo (must be done between the 1st and 30th of November)
- Settle on the title of the thesis (prefix with deep/neural?, add something to indicate the intended application?)
- Migrate repo to github once the baseline is decent *(possibly, make it an open source repo on its own and keep working on transfer across languages as a fork)*
