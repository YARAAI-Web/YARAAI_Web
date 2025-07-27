rule auto_rule_20250726213334_3424 {
  strings:
    $o0 = "dword_41DA98" wide ascii nocase
    $o1 = "tagTEXTMETRICA" wide ascii nocase
  condition:
    all of them
}