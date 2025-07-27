rule auto_rule_20250726125525_1499 {
  strings:
    $o0 = "dword_41A020" wide ascii nocase
    $o1 = "dword_454F5C" wide ascii nocase
    $o2 = "cause" wide ascii nocase
    $o3 = "__crtInitCritSecNoSpinCount" wide ascii nocase
  condition:
    4 of ($o*)
}