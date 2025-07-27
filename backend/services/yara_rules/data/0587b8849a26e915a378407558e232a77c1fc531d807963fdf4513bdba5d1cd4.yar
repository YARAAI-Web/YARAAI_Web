rule auto_rule_20250727005013_3916 {
  strings:
    $o0 = "ActiveWindow" wide ascii nocase
    $o1 = "dword_45D264" wide ascii nocase
  condition:
    all of them
}