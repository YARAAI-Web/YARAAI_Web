rule auto_rule_20250726132317_5225 {
  strings:
    $o0 = "dword_6402E984" wide ascii nocase
    $o1 = "pclsid" wide ascii nocase
  condition:
    all of them
}