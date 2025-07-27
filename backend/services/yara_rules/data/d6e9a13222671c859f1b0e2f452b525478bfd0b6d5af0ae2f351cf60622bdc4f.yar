rule auto_rule_20250726072159_6865 {
  strings:
    $o0 = "x28341332EE13197ELL" wide ascii nocase
    $o1 = "x5FA12DE08F828F84LL" wide ascii nocase
    $o2 = "xE6F3FE704B8D6273uLL" wide ascii nocase
    $o3 = "v267" wide ascii nocase
  condition:
    4 of ($o*)
}