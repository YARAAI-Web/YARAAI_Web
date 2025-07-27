rule auto_rule_20250726195342_8071 {
  strings:
    $o0 = "pclsidHandler" wide ascii nocase
  condition:
    all of them
}