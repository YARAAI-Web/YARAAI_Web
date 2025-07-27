rule auto_rule_20250726124651_7303 {
  strings:
    $o0 = "__crtInitCritSecNoSpinCount" wide ascii nocase
    $o1 = "UnwindUp2_0" wide ascii nocase
    $o2 = "dword_443460" wide ascii nocase
  condition:
    3 of ($o*)
}