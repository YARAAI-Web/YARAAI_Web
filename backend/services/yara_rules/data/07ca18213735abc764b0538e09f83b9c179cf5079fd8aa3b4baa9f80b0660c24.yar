rule auto_rule_20250726122127_3839 {
  strings:
    $o0 = "dword_46A0B0" wide ascii nocase
    $o1 = "_isctype" wide ascii nocase
  condition:
    all of them
}