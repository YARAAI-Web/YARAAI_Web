rule auto_rule_20250727035238_6799 {
  strings:
    $o0 = "dword_465840" wide ascii nocase
    $o1 = "off_464240" wide ascii nocase
  condition:
    all of them
}