rule auto_rule_20250726211434_6284 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "dword_462004" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
    $o3 = "Offset" wide ascii nocase
  condition:
    4 of ($o*)
}