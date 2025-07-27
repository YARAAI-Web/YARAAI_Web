rule auto_rule_20250726120222_9045 {
  strings:
    $o0 = "x481D00000403LL" wide ascii nocase
    $o1 = "xF0Fu" wide ascii nocase
    $o2 = "dword_42E310" wide ascii nocase
    $o3 = "x412" wide ascii nocase
    $o4 = "x608Bu" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726120225_5269 {
  strings:
    $o0 = "x63C18612" wide ascii nocase
    $o1 = "x8FEC9A90B92FABF3uLL" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726120228_7123 {
  condition:
    auto_rule_20250726120222_9045 or auto_rule_20250726120225_5269
}