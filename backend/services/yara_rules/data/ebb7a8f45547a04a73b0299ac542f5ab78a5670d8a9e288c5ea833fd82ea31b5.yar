rule auto_rule_20250726172802_6738 {
  strings:
    $o0 = "dword_7F908" wide ascii nocase
    $o1 = "SysEvtC" wide ascii nocase
  condition:
    all of them
}