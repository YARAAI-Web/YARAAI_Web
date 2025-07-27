rule auto_rule_20250727002337_3022 {
  strings:
    $o0 = "dword_476464" wide ascii nocase
    $o1 = "off_476A54" wide ascii nocase
  condition:
    all of them
}