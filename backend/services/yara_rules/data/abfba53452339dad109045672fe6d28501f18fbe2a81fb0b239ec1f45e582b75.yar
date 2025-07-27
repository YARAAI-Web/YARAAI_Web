rule auto_rule_20250726120750_4703 {
  strings:
    $o0 = "wMsgFilterMax" wide ascii nocase
    $o1 = "hWndNewViewer" wide ascii nocase
    $o2 = "nVirtKey" wide ascii nocase
    $o3 = "SetClipboardData" wide ascii nocase
    $o4 = "UnpackDDElParam" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726120753_6698 {
  strings:
    $o0 = "FreeDDElParam" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726120758_2591 {
  condition:
    auto_rule_20250726120750_4703 or auto_rule_20250726120753_6698
}