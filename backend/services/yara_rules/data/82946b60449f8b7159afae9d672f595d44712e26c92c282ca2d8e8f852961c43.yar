rule auto_rule_20250727023846_8556 {
  strings:
    $o0 = "dword_10004464" wide ascii nocase
  condition:
    all of them
}