rule auto_rule_20250726115935_5026 {
  strings:
    $o0 = "dword_4762E0" wide ascii nocase
    $o1 = "dword_475F9C" wide ascii nocase
    $o2 = "_global_unwind2" wide ascii nocase
  condition:
    3 of ($o*)
}