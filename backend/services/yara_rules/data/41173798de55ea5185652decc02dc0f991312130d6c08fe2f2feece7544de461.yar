rule auto_rule_20250726113318_1489 {
  strings:
    $o0 = "VisualC" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_468058" wide ascii nocase
    $o3 = "byte_4691C0" wide ascii nocase
    $o4 = "subtype" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726113321_8361 {
  strings:
    $o0 = "_CrtSetDbgFlag" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726113324_9763 {
  condition:
    auto_rule_20250726113318_1489 or auto_rule_20250726113321_8361
}