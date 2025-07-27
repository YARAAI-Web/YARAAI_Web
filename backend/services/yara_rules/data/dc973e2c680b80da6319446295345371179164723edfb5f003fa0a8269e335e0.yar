rule auto_rule_20250726081238_7438 {
  strings:
    $o0 = "x2650FA8Fu" wide ascii nocase
    $o1 = "BitmapName" wide ascii nocase
    $o2 = "dword_413C0C" wide ascii nocase
  condition:
    3 of ($o*)
}