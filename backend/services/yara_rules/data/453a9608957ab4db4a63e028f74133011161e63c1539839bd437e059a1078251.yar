rule auto_rule_20250726222726_6782 {
  strings:
    $o0 = "_cftof_g" wide ascii nocase
    $o1 = "allocated" wide ascii nocase
    $o2 = "dword_46D5B0" wide ascii nocase
    $o3 = "dword_46CAB4" wide ascii nocase
  condition:
    4 of ($o*)
}