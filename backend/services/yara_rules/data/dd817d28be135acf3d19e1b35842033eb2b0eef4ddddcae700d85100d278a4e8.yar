rule auto_rule_20250726235154_0890 {
  strings:
    $o0 = "dword_427984" wide ascii nocase
  condition:
    all of them
}