rule auto_rule_20250727043107_8444 {
  strings:
    $o0 = "__crtInitCritSecNoSpinCount" wide ascii nocase
    $o1 = "fill_with_EOS_dwords" wide ascii nocase
    $o2 = "_SEH_epilog" wide ascii nocase
    $o3 = "dword_46ED5C" wide ascii nocase
  condition:
    4 of ($o*)
}