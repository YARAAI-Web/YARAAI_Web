rule auto_rule_20250726182343_8426 {
  strings:
    $o0 = "x1E9DEF79" wide ascii nocase
    $o1 = "x4E6Eu" wide ascii nocase
    $o2 = "x106000004F6DLL" wide ascii nocase
    $o3 = "x3823" wide ascii nocase
  condition:
    4 of ($o*)
}