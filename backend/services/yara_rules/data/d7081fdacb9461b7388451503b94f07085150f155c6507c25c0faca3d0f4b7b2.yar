rule auto_rule_20250726114042_0659 {
  strings:
    $o0 = "bErase" wide ascii nocase
    $o1 = "GetDoubleClickTime" wide ascii nocase
    $o2 = "dwDesiredAccess" wide ascii nocase
    $o3 = "lResult" wide ascii nocase
    $o4 = "GetInputDesktop" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726114044_0742 {
  strings:
    $o0 = "aS2ftware" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726114053_4119 {
  condition:
    auto_rule_20250726114042_0659 or auto_rule_20250726114044_0742
}