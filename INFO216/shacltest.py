from pyshacl import validate
r = validate(data_graph,
      shacl_graph=sg,
      ont_graph=og,
      inference='rdfs',
      abort_on_first=False,
      allow_infos=False,
      allow_warnings=False,
      meta_shacl=False,
      advanced=False,
      js=False,
      debug=False)
conforms, results_graph, results_text = r