rule auto_rule_20250726202413_7433 {
  strings:
    $o0 = "dword_477068" wide ascii nocase
  condition:
    all of them
}