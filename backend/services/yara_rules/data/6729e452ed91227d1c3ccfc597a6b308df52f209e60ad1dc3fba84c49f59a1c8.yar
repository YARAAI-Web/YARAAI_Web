rule auto_rule_20250727033503_1533 {
  strings:
    $o0 = "dword_42FCF1" wide ascii nocase
    $o1 = "uSize" wide ascii nocase
    $o2 = "x7513u" wide ascii nocase
    $o3 = "x32729Cu" wide ascii nocase
  condition:
    4 of ($o*)
}