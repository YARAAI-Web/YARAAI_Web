rule auto_rule_20250726235551_1212 {
  strings:
    $o0 = "byte_40A749" wide ascii nocase
    $o1 = "x69FBu" wide ascii nocase
    $o2 = "x64AF" wide ascii nocase
    $o3 = "dword_41009F" wide ascii nocase
    $o4 = "x5221" wide ascii nocase
  condition:
    4 of ($o*)
}