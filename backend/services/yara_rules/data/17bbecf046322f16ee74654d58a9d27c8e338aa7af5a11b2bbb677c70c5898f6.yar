rule auto_rule_20250726224933_0826 {
  strings:
    $o0 = "__crtMessageBoxA" wide ascii nocase
    $o1 = "dword_45D53C" wide ascii nocase
    $o2 = "_except_handler3" wide ascii nocase
  condition:
    3 of ($o*)
}