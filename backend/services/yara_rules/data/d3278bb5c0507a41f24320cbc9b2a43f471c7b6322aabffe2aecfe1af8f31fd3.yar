rule auto_rule_20250727035702_8411 {
  strings:
    $o0 = "dword_4032D4" wide ascii nocase
  condition:
    all of them
}