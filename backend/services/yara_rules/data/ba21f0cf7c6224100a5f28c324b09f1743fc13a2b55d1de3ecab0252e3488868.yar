rule auto_rule_20250727042929_1463 {
  strings:
    $o0 = "dword_447030" wide ascii nocase
    $o1 = "StringTypeA" wide ascii nocase
    $o2 = "__freetlocinfo" wide ascii nocase
    $o3 = "dword_447010" wide ascii nocase
  condition:
    4 of ($o*)
}