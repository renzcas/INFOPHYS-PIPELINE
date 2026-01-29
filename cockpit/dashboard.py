def render_step(step_data: dict):
    print(f"t={step_data['time']:.3f}, dt={step_data['dt']:.3f}")
    print(f"  Lagrangian: {step_data['physics']['L']:.4f}, Action: {step_data['action']:.4f}")
    print(f"  Attention gain: {step_data['mind']['attention_gain']:.4f}")
    print(f"  Dominant freq: {step_data['compute']['dominant_freq']:.4f}")
    print("-" * 40)