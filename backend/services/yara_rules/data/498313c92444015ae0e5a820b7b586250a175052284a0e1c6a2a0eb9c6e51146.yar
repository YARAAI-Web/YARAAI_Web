rule auto_rule_20250726073210_7206 {
  strings:
    $o0 = "hrgnUpdate" wide ascii nocase
    $o1 = "pptDst" wide ascii nocase
    $o2 = "flAllocationType" wide ascii nocase
    $o3 = "MenuItemFromPoint" wide ascii nocase
    $o4 = "hszTopic" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726073213_1269 {
  strings:
    $o0 = "fByPos" wide ascii nocase
    $o1 = "hwinsta" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726073217_4552 {
  condition:
    auto_rule_20250726073210_7206 or auto_rule_20250726073213_1269
}