rule auto_rule_20250726131218_5277 {
  strings:
    $o0 = "lpOutputFunc" wide ascii nocase
    $o1 = "wData" wide ascii nocase
    $o2 = "RealGetWindowClassA" wide ascii nocase
    $o3 = "ChangeDisplaySettingsA" wide ascii nocase
    $o4 = "GetInputDesktop" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726131220_4055 {
  strings:
    $o0 = "iItem" wide ascii nocase
    $o1 = "TranslateMDISysAccel" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726131225_1832 {
  condition:
    auto_rule_20250726131218_5277 or auto_rule_20250726131220_4055
}