rule auto_rule_20250727040144_1380 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "atol" wide ascii nocase
    $o2 = "dword_45C2D0" wide ascii nocase
    $o3 = "__crtInitCritSecNoSpinCount" wide ascii nocase
  condition:
    4 of ($o*)
}