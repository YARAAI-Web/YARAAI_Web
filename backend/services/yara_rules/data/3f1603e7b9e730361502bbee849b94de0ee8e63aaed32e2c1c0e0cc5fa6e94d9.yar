rule auto_rule_20250726214017_3695 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "dword_45D160" wide ascii nocase
    $o2 = "__crtInitCritSecAndSpinCount" wide ascii nocase
    $o3 = "UnwindUp2_0" wide ascii nocase
    $o4 = "__sbh_alloc_block" wide ascii nocase
  condition:
    5 of ($o*)
}