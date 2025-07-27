rule auto_rule_20250726182630_7289 {
  strings:
    $o0 = "dword_42EEB4" wide ascii nocase
    $o1 = "dwDesiredAccess" wide ascii nocase
  condition:
    all of them
}