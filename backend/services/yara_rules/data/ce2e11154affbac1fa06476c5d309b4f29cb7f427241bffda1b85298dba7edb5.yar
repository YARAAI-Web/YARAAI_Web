rule auto_rule_20250726090253_2076 {
  strings:
    $o0 = "ScrollWindow" wide ascii nocase
    $o1 = "pSessionId" wide ascii nocase
    $o2 = "HeapUnlock" wide ascii nocase
    $o3 = "lpCreationTime" wide ascii nocase
    $o4 = "MapVirtualKeyA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726090255_6897 {
  strings:
    $o0 = "dword_447F3C" wide ascii nocase
    $o1 = "hszTopic" wide ascii nocase
    $o2 = "hConsoleInput" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726090259_5820 {
  condition:
    auto_rule_20250726090253_2076 or auto_rule_20250726090255_6897
}