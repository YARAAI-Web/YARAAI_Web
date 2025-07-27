rule auto_rule_20250726071518_6865 {
  strings:
    $o0 = "lpDefaultChar" wide ascii nocase
    $o1 = "dword_466000" wide ascii nocase
  condition:
    all of them
}