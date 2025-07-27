rule auto_rule_20250726220847_9907 {
  strings:
    $o0 = "_cftof_g" wide ascii nocase
    $o1 = "dword_427E34" wide ascii nocase
    $o2 = "dword_4275C4" wide ascii nocase
    $o3 = "_cfltcvt_init" wide ascii nocase
  condition:
    4 of ($o*)
}