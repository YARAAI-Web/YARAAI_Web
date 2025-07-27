rule auto_rule_20250727040941_4110 {
  strings:
    $o0 = "TrailDown1" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "dword_44C3F0" wide ascii nocase
  condition:
    3 of ($o*)
}