cwlVersion: v1.0
steps:
  read-potential-cases-disc:
    run: read-potential-cases-disc.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule1
      potentialCases:
        id: potentialCases
        source: potentialCases
  hypomanic-bipolar-disorder-and-other-mood-related-disorders---primary:
    run: hypomanic-bipolar-disorder-and-other-mood-related-disorders---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule2
      potentialCases:
        id: potentialCases
        source: read-potential-cases-disc/output
  bipolar-disorder-and-other-mood-related-disorders-depre---primary:
    run: bipolar-disorder-and-other-mood-related-disorders-depre---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule3
      potentialCases:
        id: potentialCases
        source: hypomanic-bipolar-disorder-and-other-mood-related-disorders---primary/output
  bipolar-disorder-and-other-mood-related-disorders-affectsevere---primary:
    run: bipolar-disorder-and-other-mood-related-disorders-affectsevere---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule4
      potentialCases:
        id: potentialCases
        source: bipolar-disorder-and-other-mood-related-disorders-depre---primary/output
  bipolar-disorder-and-other-mood-related-disorders-psych---primary:
    run: bipolar-disorder-and-other-mood-related-disorders-psych---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule5
      potentialCases:
        id: potentialCases
        source: bipolar-disorder-and-other-mood-related-disorders-affectsevere---primary/output
  effective-bipolar-disorder-and-other-mood-related-disorders---primary:
    run: effective-bipolar-disorder-and-other-mood-related-disorders---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule6
      potentialCases:
        id: potentialCases
        source: bipolar-disorder-and-other-mood-related-disorders-psych---primary/output
  bipolar-disorder-and-other-mood-related-disorders-bipolaffectpart---primary:
    run: bipolar-disorder-and-other-mood-related-disorders-bipolaffectpart---primary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule7
      potentialCases:
        id: potentialCases
        source: effective-bipolar-disorder-and-other-mood-related-disorders---primary/output
  output-cases:
    run: output-cases.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule8
      potentialCases:
        id: potentialCases
        source: bipolar-disorder-and-other-mood-related-disorders-bipolaffectpart---primary/output
class: Workflow
inputs:
  potentialCases:
    id: potentialCases
    doc: Input of potential cases for processing
    type: File
  inputModule1:
    id: inputModule1
    doc: Python implementation unit
    type: File
  inputModule2:
    id: inputModule2
    doc: Python implementation unit
    type: File
  inputModule3:
    id: inputModule3
    doc: Python implementation unit
    type: File
  inputModule4:
    id: inputModule4
    doc: Python implementation unit
    type: File
  inputModule5:
    id: inputModule5
    doc: Python implementation unit
    type: File
  inputModule6:
    id: inputModule6
    doc: Python implementation unit
    type: File
  inputModule7:
    id: inputModule7
    doc: Python implementation unit
    type: File
  inputModule8:
    id: inputModule8
    doc: Python implementation unit
    type: File
outputs:
  cases:
    id: cases
    type: File
    outputSource: output-cases/output
    outputBinding:
      glob: '*.csv'
requirements:
  SubworkflowFeatureRequirement: {}
