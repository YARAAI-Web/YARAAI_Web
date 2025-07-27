rule auto_rule_20250726102131_4128 {
  strings:
    $o0 = "x64000000" wide ascii nocase
    $o1 = "pclsid" wide ascii nocase
  condition:
    all of them
}