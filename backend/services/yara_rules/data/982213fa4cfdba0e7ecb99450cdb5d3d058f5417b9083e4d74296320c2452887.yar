rule auto_rule_20250726151917_3584 {
  strings:
    $o0 = "old_esp" wide ascii nocase
    $o1 = "UnwindUp6_0" wide ascii nocase
    $o2 = "dword_446040" wide ascii nocase
    $o3 = "dword_445EBC" wide ascii nocase
  condition:
    4 of ($o*)
}