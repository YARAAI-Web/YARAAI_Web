rule auto_rule_20250727042314_9628 {
  strings:
    $o0 = "dword_464404" wide ascii nocase
    $o1 = "dword_46428C" wide ascii nocase
  condition:
    all of them
}