rule auto_rule_20250726113915_0519 {
  strings:
    $o0 = "dword_41199C" wide ascii nocase
    $o1 = "dword_411E44" wide ascii nocase
    $o2 = "_except_handler3" wide ascii nocase
  condition:
    3 of ($o*)
}