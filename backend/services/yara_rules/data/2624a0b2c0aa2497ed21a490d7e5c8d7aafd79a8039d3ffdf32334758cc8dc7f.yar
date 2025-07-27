rule auto_rule_20250726221709_8635 {
  strings:
    $o0 = "dword_46ED48" wide ascii nocase
    $o1 = "ReturnValue" wide ascii nocase
    $o2 = "_setenvp" wide ascii nocase
    $o3 = "dword_46EBC8" wide ascii nocase
    $o4 = "CopyUnwindUp_0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726221712_6779 {
  strings:
    $o0 = "off_46E74C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726221717_4291 {
  condition:
    auto_rule_20250726221709_8635 or auto_rule_20250726221712_6779
}