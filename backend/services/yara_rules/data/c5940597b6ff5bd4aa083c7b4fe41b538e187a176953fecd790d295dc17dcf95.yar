rule auto_rule_20250727023341_3436 {
  strings:
    $o0 = "dword_106BF864" wide ascii nocase
  condition:
    all of them
}