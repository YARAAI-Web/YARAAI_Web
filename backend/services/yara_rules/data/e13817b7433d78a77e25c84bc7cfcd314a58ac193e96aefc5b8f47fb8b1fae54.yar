rule auto_rule_20250726110543_0693 {
  strings:
    $o0 = "x49E200003776LL" wide ascii nocase
    $o1 = "dword_429991" wide ascii nocase
    $o2 = "x28C1" wide ascii nocase
    $o3 = "x5EB4" wide ascii nocase
    $o4 = "x7B6AB626u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726110546_5776 {
  strings:
    $o0 = "dword_4298C1" wide ascii nocase
    $o1 = "dword_429544" wide ascii nocase
    $o2 = "x5894u" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726110550_2504 {
  condition:
    auto_rule_20250726110543_0693 or auto_rule_20250726110546_5776
}