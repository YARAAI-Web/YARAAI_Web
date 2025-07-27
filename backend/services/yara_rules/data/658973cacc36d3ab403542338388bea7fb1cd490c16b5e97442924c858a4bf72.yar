rule auto_rule_20250727005422_1085 {
  strings:
    $o0 = "dword_41A0E8" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "x300u" wide ascii nocase
    $o3 = "_cfltcvt_init" wide ascii nocase
    $o4 = "dword_4849D0" wide ascii nocase
  condition:
    4 of ($o*)
}