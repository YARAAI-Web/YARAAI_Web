rule auto_rule_20250726141852_4537 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "dword_4798B8" wide ascii nocase
    $o2 = "_heap_alloc" wide ascii nocase
    $o3 = "GetStringTypeA" wide ascii nocase
    $o4 = "Handler" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726141854_1380 {
  strings:
    $o0 = "off_479420" wide ascii nocase
    $o1 = "cause" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726141906_7397 {
  condition:
    auto_rule_20250726141852_4537 or auto_rule_20250726141854_1380
}